





import java.util.List;
import java.util.ArrayList;

public class Item  {

    private String ImagePath2;
    private String MinPreviewImagePath;
    private String ImagePath3;
    private String PreviewImagePath;
    private String Name;
    private String Brand;
    private String Description;
    private String Size;
    private int Sex;
    private String CategoryId;
    private String Color;
    private int Status;
    private String Discount;
    private String Price;
    private int Amount;
    private String ImagePath1;
    private String SubCategoryId;



    public Item(
        String ImagePath2,        String MinPreviewImagePath,        String ImagePath3,        String PreviewImagePath,        String Name,        String Brand,        String Description,        String Size,        int Sex,        String CategoryId,        String Color,        int Status,        String Discount,        String Price,        int Amount,        String ImagePath1,        String SubCategoryId    ) {
        this.ImagePath2 = ImagePath2;
        this.MinPreviewImagePath = MinPreviewImagePath;
        this.ImagePath3 = ImagePath3;
        this.PreviewImagePath = PreviewImagePath;
        this.Name = Name;
        this.Brand = Brand;
        this.Description = Description;
        this.Size = Size;
        this.Sex = Sex;
        this.CategoryId = CategoryId;
        this.Color = Color;
        this.Status = Status;
        this.Discount = Discount;
        this.Price = Price;
        this.Amount = Amount;
        this.ImagePath1 = ImagePath1;
        this.SubCategoryId = SubCategoryId;
    }


    public String getImagepath2() {
        return ImagePath2;
    }

    public void setImagepath2(String ImagePath2) {
        this.ImagePath2 = ImagePath2;
    }
    public String getMinpreviewimagepath() {
        return MinPreviewImagePath;
    }

    public void setMinpreviewimagepath(String MinPreviewImagePath) {
        this.MinPreviewImagePath = MinPreviewImagePath;
    }
    public String getImagepath3() {
        return ImagePath3;
    }

    public void setImagepath3(String ImagePath3) {
        this.ImagePath3 = ImagePath3;
    }
    public String getPreviewimagepath() {
        return PreviewImagePath;
    }

    public void setPreviewimagepath(String PreviewImagePath) {
        this.PreviewImagePath = PreviewImagePath;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getBrand() {
        return Brand;
    }

    public void setBrand(String Brand) {
        this.Brand = Brand;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
    }
    public int getSex() {
        return Sex;
    }

    public void setSex(int Sex) {
        this.Sex = Sex;
    }
    public String getCategoryid() {
        return CategoryId;
    }

    public void setCategoryid(String CategoryId) {
        this.CategoryId = CategoryId;
    }
    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public int getStatus() {
        return Status;
    }

    public void setStatus(int Status) {
        this.Status = Status;
    }
    public String getDiscount() {
        return Discount;
    }

    public void setDiscount(String Discount) {
        this.Discount = Discount;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }
    public String getImagepath1() {
        return ImagePath1;
    }

    public void setImagepath1(String ImagePath1) {
        this.ImagePath1 = ImagePath1;
    }
    public String getSubcategoryid() {
        return SubCategoryId;
    }

    public void setSubcategoryid(String SubCategoryId) {
        this.SubCategoryId = SubCategoryId;
    }


}