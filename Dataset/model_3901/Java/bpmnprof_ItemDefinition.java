





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ItemDefinition extends RootElement {

    private String itemKind;
    private String isCollection;





    private bpmnprof_ItemAwareElement bpmnprof_itemawareelement;




    private bpmnprof_Class bpmnprof_class;




    private bpmnprof_Element bpmnprof_element;




    private bpmnprof_ResourceParameter bpmnprof_resourceparameter;




    private bpmnprof_Import bpmnprof_import;




    private bpmnprof_CorrelationProperty bpmnprof_correlationproperty;




    private bpmnprof_DataStore bpmnprof_datastore;


    public bpmnprof_ItemDefinition(
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

    public bpmnprof_ItemAwareElement getBpmnprof_itemawareelement() {
        return bpmnprof_itemawareelement;
    }

    public void setBpmnprof_itemawareelement(bpmnprof_ItemAwareElement bpmnprof_itemawareelement) {
        this.bpmnprof_itemawareelement = bpmnprof_itemawareelement;
    }
    public bpmnprof_Class getBpmnprof_class() {
        return bpmnprof_class;
    }

    public void setBpmnprof_class(bpmnprof_Class bpmnprof_class) {
        this.bpmnprof_class = bpmnprof_class;
    }
    public bpmnprof_Element getBpmnprof_element() {
        return bpmnprof_element;
    }

    public void setBpmnprof_element(bpmnprof_Element bpmnprof_element) {
        this.bpmnprof_element = bpmnprof_element;
    }
    public bpmnprof_ResourceParameter getBpmnprof_resourceparameter() {
        return bpmnprof_resourceparameter;
    }

    public void setBpmnprof_resourceparameter(bpmnprof_ResourceParameter bpmnprof_resourceparameter) {
        this.bpmnprof_resourceparameter = bpmnprof_resourceparameter;
    }
    public bpmnprof_Import getBpmnprof_import() {
        return bpmnprof_import;
    }

    public void setBpmnprof_import(bpmnprof_Import bpmnprof_import) {
        this.bpmnprof_import = bpmnprof_import;
    }
    public bpmnprof_CorrelationProperty getBpmnprof_correlationproperty() {
        return bpmnprof_correlationproperty;
    }

    public void setBpmnprof_correlationproperty(bpmnprof_CorrelationProperty bpmnprof_correlationproperty) {
        this.bpmnprof_correlationproperty = bpmnprof_correlationproperty;
    }
    public bpmnprof_DataStore getBpmnprof_datastore() {
        return bpmnprof_datastore;
    }

    public void setBpmnprof_datastore(bpmnprof_DataStore bpmnprof_datastore) {
        this.bpmnprof_datastore = bpmnprof_datastore;
    }

}