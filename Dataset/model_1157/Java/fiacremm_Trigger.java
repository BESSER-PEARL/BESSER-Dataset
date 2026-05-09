





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Trigger extends EModelElement {

    private String Name;
    private int ArgSize;
    private String Body;
    private String codeFiacre;





    private List<fiacremm_Variable> fiacremm_variables;


    public fiacremm_Trigger(
        String Name,        int ArgSize,        String Body,        String codeFiacre    ) {
        super(
        );
        this.Name = Name;
        this.ArgSize = ArgSize;
        this.Body = Body;
        this.codeFiacre = codeFiacre;
        this.fiacremm_variables = new ArrayList<>();
    }

    public fiacremm_Trigger(
        String Name,        int ArgSize,        String Body,        String codeFiacre        ArrayList<fiacremm_Variable> fiacremm_variables    ) {
        this.Name = Name;
        this.ArgSize = ArgSize;
        this.Body = Body;
        this.codeFiacre = codeFiacre;
        this.fiacremm_variables = fiacremm_variables;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getArgsize() {
        return ArgSize;
    }

    public void setArgsize(int ArgSize) {
        this.ArgSize = ArgSize;
    }
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getCodefiacre() {
        return codeFiacre;
    }

    public void setCodefiacre(String codeFiacre) {
        this.codeFiacre = codeFiacre;
    }

    public List<fiacremm_Variable> getFiacremm_variables() {
        return fiacremm_variables;
    }

    public void addFiacremm_variable(Fiacremm_variable fiacremm_variable) {
        this.fiacremm_variables.add(fiacremm_variable);
    }

}