





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_DataType extends Classifier {






    private CompleteDSLPckg_Property completedslpckg_property;




    private List<CompleteDSLPckg_Property> completedslpckg_propertys;


    public CompleteDSLPckg_DataType(
    ) {
        super(
        );
        this.completedslpckg_propertys = new ArrayList<>();
    }

    public CompleteDSLPckg_DataType(
        ArrayList<CompleteDSLPckg_Property> completedslpckg_propertys    ) {
        this.completedslpckg_propertys = completedslpckg_propertys;
    }


    public CompleteDSLPckg_Property getCompletedslpckg_property() {
        return completedslpckg_property;
    }

    public void setCompletedslpckg_property(CompleteDSLPckg_Property completedslpckg_property) {
        this.completedslpckg_property = completedslpckg_property;
    }
    public List<CompleteDSLPckg_Property> getCompletedslpckg_propertys() {
        return completedslpckg_propertys;
    }

    public void addCompletedslpckg_property(Completedslpckg_property completedslpckg_property) {
        this.completedslpckg_propertys.add(completedslpckg_property);
    }

}