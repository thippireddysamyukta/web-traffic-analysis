import pandas as pd

# Step 1: Create dataset
data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "page_visited": ["Home", "Products", "Home", "Pricing", "Products", 
                     "About Us", "Blog", "Pricing", "Contact", "Products"],
    "session_duration_min": [2.5, 5.1, 1.2, 4.35, 6.0, 3.2, 2.8, 4.9, 0.5, 7.2],
    "pages_viewed": [3, 5, 1, 4, 6, 3, 2, 4, 1, 8],
    "exited": [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
print(df)

# Step 2: Most visited pages
print("=== PAGE VIEWS ===")
print(df["page_visited"].value_counts())

print("\n=== AVG TIME ON PAGE (minutes) ===")
print(df.groupby("page_visited")["session_duration_min"].mean().round(2).sort_values(ascending=False))

# Step 3: Exit and bounce rates
print("=== EXIT RATE PER PAGE ===")
exit_rate = df.groupby("page_visited")["exited"].mean() * 100
print(exit_rate.round(1).sort_values(ascending=False))

print(f"\nOverall exit rate: {df['exited'].mean()*100}%")
bounced = df[df["pages_viewed"] == 1]
print(f"Bounce rate: {len(bounced)/len(df)*100}%")

# Step 4: Summary
df.to_csv("web_traffic_analysis.csv", index=False)
print("=== WEB TRAFFIC ANALYSIS SUMMARY ===")
print(f"Total users: {len(df)}")
print(f"Most visited page: {df['page_visited'].value_counts().idxmax()}")
print(f"Avg session duration: {df['session_duration_min'].mean().round(2)} mins")
print(f"Overall exit rate: {df['exited'].mean()*100}%")
print(f"Bounce rate: {len(df[df['pages_viewed']==1])/len(df)*100}%")
print("\nDrop-off points:")
print("1. Blog - 100% exit rate")
print("2. Contact - 100% exit rate")
print("\nUser Journey: Home → Products → Pricing → (exit or convert)")
print("\nRecommendations:")
print("1. Add CTAs on Blog to guide users to Products")
print("2. Improve Contact page to reduce exits")
print("3. Products & Pricing pages are working well - keep them engaging!")
print("\n✅ Saved to web_traffic_analysis.csv!")
