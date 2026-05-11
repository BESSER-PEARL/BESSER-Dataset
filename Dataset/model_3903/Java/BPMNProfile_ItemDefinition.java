





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ItemDefinition extends RootElement {

    private String itemKind;
    private String isCollection;





    private BPMNProfile_ItemAwareElement bpmnprofile_itemawareelement;




    private BPMNProfile_Class bpmnprofile_class;




    private BPMNProfile_Import bpmnprofile_import;




    private BPMNProfile_DataStore bpmnprofile_datastore;




    private BPMNProfile_ResourceParameter bpmnprofile_resourceparameter;




    private BPMNProfile_Element bpmnprofile_element;




    private BPMNProfile_CorrelationProperty bpmnprofile_correlationproperty;


    public BPMNProfile_ItemDefinition(
        String itemKind,        String isCollection    ) {
        super(
        );
        this.itemKind = itemKind;
        this.isCollection = isCollection;
    }


    public String getItemkind() {
        return itemKind;
    }

    public void setItemkind(String itemKind) {
        this.itemKind = itemKind;
    }
    public String getIscollection() {
        return isCollection;
    }

    public void setIscollection(String isCollection) {
        this.isCollection = isCollection;
    }

    public BPMNProfile_ItemAwareElement getBpmnprofile_itemawareelement() {
        return bpmnprofile_itemawareelement;
    }

    public void setBpmnprofile_itemawareelement(BPMNProfile_ItemAwareElement bpmnprofile_itemawareelement) {
        this.bpmnprofile_itemawareelement = bpmnprofile_itemawareelement;
    }
    public BPMNProfile_Class getBpmnprofile_class() {
        return bpmnprofile_class;
    }

    public void setBpmnprofile_class(BPMNProfile_Class bpmnprofile_class) {
        this.bpmnprofile_class = bpmnprofile_class;
    }
    public BPMNProfile_Import getBpmnprofile_import() {
        return bpmnprofile_import;
    }

    public void setBpmnprofile_import(BPMNProfile_Import bpmnprofile_import) {
        this.bpmnprofile_import = bpmnprofile_import;
    }
    public BPMNProfile_DataStore getBpmnprofile_datastore() {
        return bpmnprofile_datastore;
    }

    public void setBpmnprofile_datastore(BPMNProfile_DataStore bpmnprofile_datastore) {
        this.bpmnprofile_datastore = bpmnprofile_datastore;
    }
    public BPMNProfile_ResourceParameter getBpmnprofile_resourceparameter() {
        return bpmnprofile_resourceparameter;
    }

    public void setBpmnprofile_resourceparameter(BPMNProfile_ResourceParameter bpmnprofile_resourceparameter) {
        this.bpmnprofile_resourceparameter = bpmnprofile_resourceparameter;
    }
    public BPMNProfile_Element getBpmnprofile_element() {
        return bpmnprofile_element;
    }

    public void setBpmnprofile_element(BPMNProfile_Element bpmnprofile_element) {
        this.bpmnprofile_element = bpmnprofile_element;
    }
    public BPMNProfile_CorrelationProperty getBpmnprofile_correlationproperty() {
        return bpmnprofile_correlationproperty;
    }

    public void setBpmnprofile_correlationproperty(BPMNProfile_CorrelationProperty bpmnprofile_correlationproperty) {
        this.bpmnprofile_correlationproperty = bpmnprofile_correlationproperty;
    }

}