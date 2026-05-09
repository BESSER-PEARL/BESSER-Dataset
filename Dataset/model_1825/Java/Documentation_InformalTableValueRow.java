





import java.util.List;
import java.util.ArrayList;

public class Documentation_InformalTableValueRow  {






    private Documentation_InformalTableValueBody documentation_informaltablevaluebody;




    private List<Documentation_InformalTableValueEntry> documentation_informaltablevalueentrys;




    private Documentation_InformalTableValueHead documentation_informaltablevaluehead;


    public Documentation_InformalTableValueRow(
    ) {
        this.documentation_informaltablevalueentrys = new ArrayList<>();
    }

    public Documentation_InformalTableValueRow(
        ArrayList<Documentation_InformalTableValueEntry> documentation_informaltablevalueentrys    ) {
        this.documentation_informaltablevalueentrys = documentation_informaltablevalueentrys;
    }


    public Documentation_InformalTableValueBody getDocumentation_informaltablevaluebody() {
        return documentation_informaltablevaluebody;
    }

    public void setDocumentation_informaltablevaluebody(Documentation_InformalTableValueBody documentation_informaltablevaluebody) {
        this.documentation_informaltablevaluebody = documentation_informaltablevaluebody;
    }
    public List<Documentation_InformalTableValueEntry> getDocumentation_informaltablevalueentrys() {
        return documentation_informaltablevalueentrys;
    }

    public void addDocumentation_informaltablevalueentry(Documentation_informaltablevalueentry documentation_informaltablevalueentry) {
        this.documentation_informaltablevalueentrys.add(documentation_informaltablevalueentry);
    }
    public Documentation_InformalTableValueHead getDocumentation_informaltablevaluehead() {
        return documentation_informaltablevaluehead;
    }

    public void setDocumentation_informaltablevaluehead(Documentation_InformalTableValueHead documentation_informaltablevaluehead) {
        this.documentation_informaltablevaluehead = documentation_informaltablevaluehead;
    }

}