





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Operation extends BehavioralFeature {

    private boolean isQuery;





    private uml2CD_Class uml2cd_class;




    private uml2CD_Operation uml2cd_operation;




    private uml2CD_Class uml2cd_class;


    public uml2CD_Operation(
        boolean isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
    }


    public boolean getIsquery() {
        return isQuery;
    }

    public void setIsquery(boolean isQuery) {
        this.isQuery = isQuery;
    }

    public uml2CD_Class getUml2cd_class() {
        return uml2cd_class;
    }

    public void setUml2cd_class(uml2CD_Class uml2cd_class) {
        this.uml2cd_class = uml2cd_class;
    }
    public uml2CD_Operation getUml2cd_operation() {
        return uml2cd_operation;
    }

    public void setUml2cd_operation(uml2CD_Operation uml2cd_operation) {
        this.uml2cd_operation = uml2cd_operation;
    }
    public uml2CD_Class getUml2cd_class() {
        return uml2cd_class;
    }

    public void setUml2cd_class(uml2CD_Class uml2cd_class) {
        this.uml2cd_class = uml2cd_class;
    }

}