





import java.util.List;
import java.util.ArrayList;

public class henshin_text_ModelElement  {

    private String name;





    private henshin_text_Call henshin_text_call;




    private henshin_text_Model henshin_text_model;


    public henshin_text_ModelElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public henshin_text_Call getHenshin_text_call() {
        return henshin_text_call;
    }

    public void setHenshin_text_call(henshin_text_Call henshin_text_call) {
        this.henshin_text_call = henshin_text_call;
    }
    public henshin_text_Model getHenshin_text_model() {
        return henshin_text_model;
    }

    public void setHenshin_text_model(henshin_text_Model henshin_text_model) {
        this.henshin_text_model = henshin_text_model;
    }

}