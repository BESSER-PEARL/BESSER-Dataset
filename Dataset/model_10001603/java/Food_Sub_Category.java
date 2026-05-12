





import java.util.List;
import java.util.ArrayList;

public class Food_Sub_Category  {

    private String sub_descp;
    private String sub_name;
    private String sub_image;
    private int sub_id;



    public Food_Sub_Category(
        String sub_descp,        String sub_name,        String sub_image,        int sub_id    ) {
        this.sub_descp = sub_descp;
        this.sub_name = sub_name;
        this.sub_image = sub_image;
        this.sub_id = sub_id;
    }


    public String getSub_descp() {
        return sub_descp;
    }

    public void setSub_descp(String sub_descp) {
        this.sub_descp = sub_descp;
    }
    public String getSub_name() {
        return sub_name;
    }

    public void setSub_name(String sub_name) {
        this.sub_name = sub_name;
    }
    public String getSub_image() {
        return sub_image;
    }

    public void setSub_image(String sub_image) {
        this.sub_image = sub_image;
    }
    public int getSub_id() {
        return sub_id;
    }

    public void setSub_id(int sub_id) {
        this.sub_id = sub_id;
    }


}