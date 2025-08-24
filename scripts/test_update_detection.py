#!/usr/bin/env python3
"""
Test script to verify iconify update detection logic
"""
import requests
import os

def check_iconify_updates():
    """Test the iconify update checking logic"""
    print("🔍 Testing iconify update detection...")
    
    # Get current commit hash of iconify material-symbols.json
    try:
        response = requests.get("https://api.github.com/repos/iconify/icon-sets/commits?path=json/material-symbols.json&per_page=1")
        response.raise_for_status()
        commits = response.json()
        
        if commits:
            current_hash = commits[0]['sha']
            commit_date = commits[0]['commit']['committer']['date']
            print(f"✅ Current iconify commit: {current_hash[:8]}")
            print(f"📅 Last updated: {commit_date}")
            
            # Check if we have a stored hash
            hash_file = ".github/iconify-hash.txt"
            if os.path.exists(hash_file):
                with open(hash_file, 'r') as f:
                    stored_hash = f.read().strip()
                print(f"📁 Stored hash: {stored_hash[:8] if stored_hash else 'None'}")
                
                if current_hash != stored_hash:
                    print("🆕 UPDATE DETECTED - Icons would be regenerated!")
                    return True
                else:
                    print("✅ No updates needed")
                    return False
            else:
                print("🆕 No hash file found - First run detected!")
                # Create the hash file for testing
                os.makedirs(".github", exist_ok=True)
                with open(hash_file, 'w') as f:
                    f.write(current_hash)
                print(f"📝 Created hash file with: {current_hash[:8]}")
                return True
        else:
            print("❌ No commits found")
            return False
            
    except Exception as e:
        print(f"❌ Error checking for updates: {e}")
        return False

if __name__ == "__main__":
    update_needed = check_iconify_updates()
    print(f"\n📊 Result: Update needed = {update_needed}")
