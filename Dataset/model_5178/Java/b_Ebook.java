





import java.util.List;
import java.util.ArrayList;

public class b_Ebook  {

    private String date;
    private String category;
    private String info;
    private String label;





    private b_Model b_model;


    public b_Ebook(
        String date,        String category,        String info,        String label    ) {
        this.date = date;
        this.category = category;
        this.info = info;
        this.label = label;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public b_Model getB_model() {
        return b_model;
    }

    public void setB_model(b_Model b_model) {
        this.b_model = b_model;
    }

}