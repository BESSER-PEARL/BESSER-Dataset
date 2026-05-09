





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_LabelProxy  {

    private String text;





    private pnmlcoremodel_Page pnmlcoremodel_page;




    private pnmlcoremodel_Object pnmlcoremodel_object;


    public pnmlcoremodel_LabelProxy(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public pnmlcoremodel_Page getPnmlcoremodel_page() {
        return pnmlcoremodel_page;
    }

    public void setPnmlcoremodel_page(pnmlcoremodel_Page pnmlcoremodel_page) {
        this.pnmlcoremodel_page = pnmlcoremodel_page;
    }
    public pnmlcoremodel_Object getPnmlcoremodel_object() {
        return pnmlcoremodel_object;
    }

    public void setPnmlcoremodel_object(pnmlcoremodel_Object pnmlcoremodel_object) {
        this.pnmlcoremodel_object = pnmlcoremodel_object;
    }

}