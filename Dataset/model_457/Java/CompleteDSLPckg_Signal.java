





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Signal extends Classifier {






    private List<CompleteDSLPckg_Property> completedslpckg_propertys;




    private CompleteDSLPckg_Reception completedslpckg_reception;


    public CompleteDSLPckg_Signal(
    ) {
        super(
        );
        this.completedslpckg_propertys = new ArrayList<>();
    }

    public CompleteDSLPckg_Signal(
        ArrayList<CompleteDSLPckg_Property> completedslpckg_propertys    ) {
        this.completedslpckg_propertys = completedslpckg_propertys;
    }


    public List<CompleteDSLPckg_Property> getCompletedslpckg_propertys() {
        return completedslpckg_propertys;
    }

    public void addCompletedslpckg_property(Completedslpckg_property completedslpckg_property) {
        this.completedslpckg_propertys.add(completedslpckg_property);
    }
    public CompleteDSLPckg_Reception getCompletedslpckg_reception() {
        return completedslpckg_reception;
    }

    public void setCompletedslpckg_reception(CompleteDSLPckg_Reception completedslpckg_reception) {
        this.completedslpckg_reception = completedslpckg_reception;
    }

}