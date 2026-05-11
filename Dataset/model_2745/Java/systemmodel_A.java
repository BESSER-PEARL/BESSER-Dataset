





import java.util.List;
import java.util.ArrayList;

public class systemmodel_A extends ModelElement {

    private String multiValAtt;
    private String name;





    private List<systemmodel_C> systemmodel_cs;




    private List<systemmodel_B> systemmodel_bs;


    public systemmodel_A(
        String multiValAtt,        String name    ) {
        super(
        );
        this.multiValAtt = multiValAtt;
        this.name = name;
        this.systemmodel_cs = new ArrayList<>();
        this.systemmodel_bs = new ArrayList<>();
    }

    public systemmodel_A(
        String multiValAtt,        String name        ArrayList<systemmodel_C> systemmodel_cs,        ArrayList<systemmodel_B> systemmodel_bs    ) {
        this.multiValAtt = multiValAtt;
        this.name = name;
        this.systemmodel_cs = systemmodel_cs;
        this.systemmodel_bs = systemmodel_bs;
    }

    public String getMultivalatt() {
        return multiValAtt;
    }

    public void setMultivalatt(String multiValAtt) {
        this.multiValAtt = multiValAtt;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<systemmodel_C> getSystemmodel_cs() {
        return systemmodel_cs;
    }

    public void addSystemmodel_c(Systemmodel_c systemmodel_c) {
        this.systemmodel_cs.add(systemmodel_c);
    }
    public List<systemmodel_B> getSystemmodel_bs() {
        return systemmodel_bs;
    }

    public void addSystemmodel_b(Systemmodel_b systemmodel_b) {
        this.systemmodel_bs.add(systemmodel_b);
    }

}