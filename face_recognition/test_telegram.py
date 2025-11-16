#!/usr/bin/env python3
"""
Test script for Telegram notification system
"""

from telegram_notification import send_telegram_message, send_telegram_location

# Test data
test_location = {
    'city': 'Delhi',
    'region': 'NCR', 
    'country': 'India',
    'latitude': 28.7041,
    'longitude': 77.1025
}

print("🧪 Testing Telegram Notification System...\n")

# Test 1: Send text message
print("📝 Test 1: Sending text message...")
result1 = send_telegram_message(
    phone_number='9876543210',
    name='Test Person',
    adhaar='123456789012',
    location=test_location
)

if result1:
    print("✅ Text message test PASSED!\n")
else:
    print("❌ Text message test FAILED!\n")

# Test 2: Send location pin
print("📍 Test 2: Sending location pin...")
result2 = send_telegram_location(
    phone_number='9876543210',
    name='Test Person',
    adhaar='123456789012', 
    location=test_location
)

if result2:
    print("✅ Location pin test PASSED!\n")
else:
    print("❌ Location pin test FAILED!\n")

# Summary
print("\n" + "="*50)
if result1 and result2:
    print("🎉 All tests PASSED! Telegram integration working!")
    print("✅ Your system is ready to send notifications!")
else:
    print("⚠️  Some tests failed. Check:")
    print("   1. BOT_TOKEN is correct")
    print("   2. CHAT_ID is correct")
    print("   3. You've started the bot in Telegram")
    print("   4. Internet connection is working")
print("="*50)
