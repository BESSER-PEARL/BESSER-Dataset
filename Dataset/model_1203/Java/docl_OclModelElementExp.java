





import java.util.List;
import java.util.ArrayList;

public class docl_OclModelElementExp extends OclType {

    private String name;





    private docl_OclModel docl_oclmodel;


    public docl_OclModelElementExp(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public docl_OclModel getDocl_oclmodel() {
        return docl_oclmodel;
    }

    public void setDocl_oclmodel(docl_OclModel docl_oclmodel) {
        this.docl_oclmodel = docl_oclmodel;
    }

}