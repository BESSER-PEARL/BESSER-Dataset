





import java.util.List;
import java.util.ArrayList;

public class Food_Category  {

    private String Category_name;
    private String Category_descp;
    private int Category_id;
    private int sub_id;
    private String Category_image;



    public Food_Category(
        String Category_name,        String Category_descp,        int Category_id,        int sub_id,        String Category_image    ) {
        this.Category_name = Category_name;
        this.Category_descp = Category_descp;
        this.Category_id = Category_id;
        this.sub_id = sub_id;
        this.Category_image = Category_image;
    }


    public String getCategory_name() {
        return Category_name;
    }

    public void setCategory_name(String Category_name) {
        this.Category_name = Category_name;
    }
    public String getCategory_descp() {
        return Category_descp;
    }

    public void setCategory_descp(String Category_descp) {
        this.Category_descp = Category_descp;
    }
    public int getCategory_id() {
        return Category_id;
    }

    public void setCategory_id(int Category_id) {
        this.Category_id = Category_id;
    }
    public int getSub_id() {
        return sub_id;
    }

    public void setSub_id(int sub_id) {
        this.sub_id = sub_id;
    }
    public String getCategory_image() {
        return Category_image;
    }

    public void setCategory_image(String Category_image) {
        this.Category_image = Category_image;
    }


}