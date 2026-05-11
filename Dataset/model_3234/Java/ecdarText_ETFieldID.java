





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETFieldID  {

    private String ioType;
    private String name;





    private List<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations;


    public ecdarText_ETFieldID(
        String ioType,        String name    ) {
        this.ioType = ioType;
        this.name = name;
        this.ecdartext_etarraydeclarations = new ArrayList<>();
    }

    public ecdarText_ETFieldID(
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

    public List<ecdarText_ETArrayDeclaration> getEcdartext_etarraydeclarations() {
        return ecdartext_etarraydeclarations;
    }

    public void addEcdartext_etarraydeclaration(Ecdartext_etarraydeclaration ecdartext_etarraydeclaration) {
        this.ecdartext_etarraydeclarations.add(ecdartext_etarraydeclaration);
    }

}