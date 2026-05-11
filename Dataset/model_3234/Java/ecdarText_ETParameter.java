





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETParameter  {

    private String ioType;
    private String name;





    private ecdarText_ETSpecificationTemplate ecdartext_etspecificationtemplate;




    private ecdarText_ETType ecdartext_ettype;




    private List<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations;


    public ecdarText_ETParameter(
        String ioType,        String name    ) {
        this.ioType = ioType;
        this.name = name;
        this.ecdartext_etarraydeclarations = new ArrayList<>();
    }

    public ecdarText_ETParameter(
        String ioType,        String name        ArrayList<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations    ) {
        this.ioType = ioType;
        this.name = name;
        this.ecdartext_etarraydeclarations = ecdartext_etarraydeclarations;
    }

    public String getIotype() {
        return ioType;
    }

    public void setIotype(String ioType) {
        this.ioType = ioType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecdarText_ETSpecificationTemplate getEcdartext_etspecificationtemplate() {
        return ecdartext_etspecificationtemplate;
    }

    public void setEcdartext_etspecificationtemplate(ecdarText_ETSpecificationTemplate ecdartext_etspecificationtemplate) {
        this.ecdartext_etspecificationtemplate = ecdartext_etspecificationtemplate;
    }
    public ecdarText_ETType getEcdartext_ettype() {
        return ecdartext_ettype;
    }

    public void setEcdartext_ettype(ecdarText_ETType ecdartext_ettype) {
        this.ecdartext_ettype = ecdartext_ettype;
    }
    public List<ecdarText_ETArrayDeclaration> getEcdartext_etarraydeclarations() {
        return ecdartext_etarraydeclarations;
    }

    public void addEcdartext_etarraydeclaration(Ecdartext_etarraydeclaration ecdartext_etarraydeclaration) {
        this.ecdartext_etarraydeclarations.add(ecdartext_etarraydeclaration);
    }

}