# Customer Segmentation for WholeSale
### Unsupervised Machine Learning Project

<p align="center" style="margin-top: 20px; margin-bottom: 20px;">
<img width="40%" src="https://github.com/ThuyTran102/3__Customer_Segmentation_for_WholeSale/blob/main/images/customer_segmentation.png" alt="customer_segmentation"></img>
</p>

## Table of Contents:
- [Project Objectives](https://github.com/ThuyTran102/3__Customer_Segmentation_for_WholeSale?tab=readme-ov-file#project-objectives)
- [Project Desciption](https://github.com/ThuyTran102/3__Customer_Segmentation_for_WholeSale?tab=readme-ov-file#project-description)
- [Project Outcomes](https://github.com/ThuyTran102/3__Customer_Segmentation_for_WholeSale?tab=readme-ov-file#project-outcomes)
  - [Insights](https://github.com/ThuyTran102/3__Customer_Segmentation_for_WholeSale?tab=readme-ov-file#insights)
  - [Conclusion](https://github.com/ThuyTran102/3__Customer_Segmentation_for_WholeSale?tab=readme-ov-file#conclusion)

## Project Objectives:
In this project, we will apply unsupervised learning techniques to a real-world data set and use data visualization tools to communicate the insights gained from the analysis.

## Project Description:
The data set for this project is the "Wholesale Data" dataset containing information about various products sold by a grocery store.
The project will involve the following tasks:

-	Exploratory data analysis and pre-processing: We will import and clean the data sets, analyze and visualize the relationships between the different variables, handle missing values and outliers, and perform feature engineering as needed.
-	Unsupervised learning: We will use the Wholesale Data dataset to perform k-means clustering, hierarchical clustering, and principal component analysis (PCA) to identify patterns and group similar data points together. We will determine the optimal number of clusters and communicate the insights gained through data visualization.


## Project Outcomes:
<p align="center" style="margin-top: 20px; margin-bottom: 20px;">
<img width="60%" src="https://github.com/ThuyTran102/Unsupervised-Machine-Learning-Project/blob/main/images/Project_Outcome.png" alt="Outcome"></img>
</p>

### Insights:
From the clustering results using AgglomerativeClustering and PCA, with Principal Component 1 as the x-axis and Principal Component 2 as the y-axis, we can divide customers into 4 client groups as follows:

**1. Customer Group 1 (Blue):**
>- Low values on both Component 1 and Component 2.
>- Purchasing Behavior: Customers in this group exhibit low purchasing activity overall
>- Possible Customer Segment: **Occasional Shoppers**: These customers might be infrequent shoppers who do not have high demand for either staple goods or specialty items. They might shop occasionally or have **smaller households**.

**2. Customer Group 2 (Orange):**
> - High values on Component 1, but low values on Component 2.
> - Purchasing Behavior: This group primarily shops for daily necessities such as detergents, groceries, and milk.
> - Possible Customer Segment: **Household Shoppers**: They might be families or individuals who prioritize regular household needs over specialty items. This group could include working professionals, busy parents, or students who need consistent supplies of basic goods.

**3. Customer Group 3 (Green):**
> - Contrast to Client Group 2, this group has low values on Component 1, but high values on Component 2.
> - Purchasing Behavior: This group primarily shops for food goods such as fresh, frozen, and delicatessen items. These customers might prioritize fresh and specialty food items over basic household staples
> - Possible Customer Segment: **Food Enthusiasts**: They could include health-conscious individuals, foodies, or those **who prefer cooking with fresh ingredients. This segment might also include restaurant owners or chefs who focus on fresh produce and specialty items.**

**4. Customer Group 4 (Red):**
> - High values on both Component 1 and Component 2.
> - Purchasing Behavior: Customers have high purchasing activity. Customers in this group exhibit high purchasing activity for both daily necessities and specialty food items.
> - Possible Customer Segment: **High-Spending Shoppers**: They might be **affluent households, large families, or businesses** that require a wide variety of products. This group could also include wholesale buyers or bulk purchasers who need a mix of everyday and specialty items.

### Conclusion:

* Across the different channels and regions, there is a consistent **linear trend** where higher spending in one product category positively correlates with higher spending in another, most notably between `Milk & Grocery`, between `Grocery & Detergents_Paper`, and between `Milk & Detergents_Paper` ---> suggesting predictable purchasing patterns in purchasing behavior that can inform inventory management and promotional campaigns.

*  The analysis highlighted notable **outliers**, particularly in `Channel 2` and `Region 3`, indicating the presence of customers with significantly higher purchasing activity. These outliers present opportunities for customized loyalty programs and targeted sales approaches.
  
* `Channel 1` and `Region 1 and 2` customers generally show lower spending, suggesting they might be more price-sensitive or have less demand for these products.

* **Customer Segmentation**: The PCA and clustering analysis identified four distinct customer groups based on purchasing behavior. These groups vary significantly in their spending on everyday necessities versus specialty items. We can **categorize customers into 4 main groups** as above (`Occasional Shoppers`, `Household Shoppers`, `Food Shoppers`, `High-Spending Shoppers`) to help us better understand customer purchasing behaviors. This segmentation can be leveraged to tailor and develop targeted marketing strategies, optimize product offerings, and improve customer satisfaction by catering to the specific needs of each group. Understanding these segments allows for better inventory management and personalized customer engagement, ultimately driving business growth and customer loyalty. For example, clustering revealed high-spending customers (Cluster 4 - Red) who purchase large quantities of both staple and specialty goods, indicating a lucrative target for premium marketing strategies.
