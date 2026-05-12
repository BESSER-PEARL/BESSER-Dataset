





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private int ProductID;
    private int ColorID;
    private int InStock;
    private int SizeID;





    private List<Color> colors;




    private List<Products> productss;




    private List<Size> sizes;


    public Inventory(
        int ProductID,        int ColorID,        int InStock,        int SizeID    ) {
        this.ProductID = ProductID;
        this.ColorID = ColorID;
        this.InStock = InStock;
        this.SizeID = SizeID;
        this.colors = new ArrayList<>();
        this.productss = new ArrayList<>();
        this.sizes = new ArrayList<>();
    }

    public Inventory(
        int ProductID,        int ColorID,        int InStock,        int SizeID        ArrayList<Color> colors,        ArrayList<Products> productss,        ArrayList<Size> sizes    ) {
        this.ProductID = ProductID;
        this.ColorID = ColorID;
        this.InStock = InStock;
        this.SizeID = SizeID;
        this.colors = colors;
        this.productss = productss;
        this.sizes = sizes;
    }

    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public int getColorid() {
        return ColorID;
    }

    public void setColorid(int ColorID) {
        this.ColorID = ColorID;
    }
    public int getInstock() {
        return InStock;
    }

    public void setInstock(int InStock) {
        this.InStock = InStock;
    }
    public int getSizeid() {
        return SizeID;
    }

    public void setSizeid(int SizeID) {
        this.SizeID = SizeID;
    }

    public List<Color> getColors() {
        return colors;
    }

    public void addColor(Color color) {
        this.colors.add(color);
    }
    public List<Products> getProductss() {
        return productss;
    }

    public void addProducts(Products products) {
        this.productss.add(products);
    }
    public List<Size> getSizes() {
        return sizes;
    }

    public void addSize(Size size) {
        this.sizes.add(size);
    }

}