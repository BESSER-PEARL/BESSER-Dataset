





import java.util.List;
import java.util.ArrayList;

public class model_R4EFileContext extends R4EIDComponent {

    private String type;





    private model_R4EFileVersion model_r4efileversion;




    private model_R4EFileVersion model_r4efileversion;




    private model_R4EItem model_r4eitem;




    private List<model_R4EDelta> model_r4edeltas;


    public model_R4EFileContext(
        String type    ) {
        super(
        );
        this.type = type;
        this.model_r4edeltas = new ArrayList<>();
    }

    public model_R4EFileContext(
        String type        ArrayList<model_R4EDelta> model_r4edeltas    ) {
        this.type = type;
        this.model_r4edeltas = model_r4edeltas;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_R4EFileVersion getModel_r4efileversion() {
        return model_r4efileversion;
    }

    public void setModel_r4efileversion(model_R4EFileVersion model_r4efileversion) {
        this.model_r4efileversion = model_r4efileversion;
    }
    public model_R4EFileVersion getModel_r4efileversion() {
        return model_r4efileversion;
    }

    public void setModel_r4efileversion(model_R4EFileVersion model_r4efileversion) {
        this.model_r4efileversion = model_r4efileversion;
    }
    public model_R4EItem getModel_r4eitem() {
        return model_r4eitem;
    }

    public void setModel_r4eitem(model_R4EItem model_r4eitem) {
        this.model_r4eitem = model_r4eitem;
    }
    public List<model_R4EDelta> getModel_r4edeltas() {
        return model_r4edeltas;
    }

    public void addModel_r4edelta(Model_r4edelta model_r4edelta) {
        this.model_r4edeltas.add(model_r4edelta);
    }

}