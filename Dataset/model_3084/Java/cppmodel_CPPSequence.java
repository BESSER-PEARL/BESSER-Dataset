





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPSequence extends OOPLSequence {

    private String cppContainer;





    private cppmodel_CPPFormalParameter cppmodel_cppformalparameter;




    private cppmodel_CPPReturnValue cppmodel_cppreturnvalue;




    private cppmodel_CPPAttribute cppmodel_cppattribute;


    public cppmodel_CPPSequence(
        String cppContainer    ) {
        super(
        );
        this.cppContainer = cppContainer;
    }


    public String getCppcontainer() {
        return cppContainer;
    }

    public void setCppcontainer(String cppContainer) {
        this.cppContainer = cppContainer;
    }

    public cppmodel_CPPFormalParameter getCppmodel_cppformalparameter() {
        return cppmodel_cppformalparameter;
    }

    public void setCppmodel_cppformalparameter(cppmodel_CPPFormalParameter cppmodel_cppformalparameter) {
        this.cppmodel_cppformalparameter = cppmodel_cppformalparameter;
    }
    public cppmodel_CPPReturnValue getCppmodel_cppreturnvalue() {
        return cppmodel_cppreturnvalue;
    }

    public void setCppmodel_cppreturnvalue(cppmodel_CPPReturnValue cppmodel_cppreturnvalue) {
        this.cppmodel_cppreturnvalue = cppmodel_cppreturnvalue;
    }
    public cppmodel_CPPAttribute getCppmodel_cppattribute() {
        return cppmodel_cppattribute;
    }

    public void setCppmodel_cppattribute(cppmodel_CPPAttribute cppmodel_cppattribute) {
        this.cppmodel_cppattribute = cppmodel_cppattribute;
    }

}