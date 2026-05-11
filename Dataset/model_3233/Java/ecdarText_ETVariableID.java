





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETVariableID  {

    private String ioType;
    private String name;





    private ecdarText_ETVariableDeclaration ecdartext_etvariabledeclaration;




    private List<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations;


    public ecdarText_ETVariableID(
        String ioType,        String name    ) {
        this.ioType = ioType;
        this.name = name;
        this.ecdartext_etarraydeclarations = new ArrayList<>();
    }

    public ecdarText_ETVariableID(
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

    public ecdarText_ETVariableDeclaration getEcdartext_etvariabledeclaration() {
        return ecdartext_etvariabledeclaration;
    }

    public void setEcdartext_etvariabledeclaration(ecdarText_ETVariableDeclaration ecdartext_etvariabledeclaration) {
        this.ecdartext_etvariabledeclaration = ecdartext_etvariabledeclaration;
    }
    public List<ecdarText_ETArrayDeclaration> getEcdartext_etarraydeclarations() {
        return ecdartext_etarraydeclarations;
    }

    public void addEcdartext_etarraydeclaration(Ecdartext_etarraydeclaration ecdartext_etarraydeclaration) {
        this.ecdartext_etarraydeclarations.add(ecdartext_etarraydeclaration);
    }

}