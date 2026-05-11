





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETVariableID  {

    private String name;
    private String ioType;





    private ecdarText_ETInitialiser ecdartext_etinitialiser;




    private List<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations;




    private ecdarText_ETVariableDeclaration ecdartext_etvariabledeclaration;


    public ecdarText_ETVariableID(
        String name,        String ioType    ) {
        this.name = name;
        this.ioType = ioType;
        this.ecdartext_etarraydeclarations = new ArrayList<>();
    }

    public ecdarText_ETVariableID(
        String name,        String ioType        ArrayList<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations    ) {
        this.name = name;
        this.ioType = ioType;
        this.ecdartext_etarraydeclarations = ecdartext_etarraydeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIotype() {
        return ioType;
    }

    public void setIotype(String ioType) {
        this.ioType = ioType;
    }

    public ecdarText_ETInitialiser getEcdartext_etinitialiser() {
        return ecdartext_etinitialiser;
    }

    public void setEcdartext_etinitialiser(ecdarText_ETInitialiser ecdartext_etinitialiser) {
        this.ecdartext_etinitialiser = ecdartext_etinitialiser;
    }
    public List<ecdarText_ETArrayDeclaration> getEcdartext_etarraydeclarations() {
        return ecdartext_etarraydeclarations;
    }

    public void addEcdartext_etarraydeclaration(Ecdartext_etarraydeclaration ecdartext_etarraydeclaration) {
        this.ecdartext_etarraydeclarations.add(ecdartext_etarraydeclaration);
    }
    public ecdarText_ETVariableDeclaration getEcdartext_etvariabledeclaration() {
        return ecdartext_etvariabledeclaration;
    }

    public void setEcdartext_etvariabledeclaration(ecdarText_ETVariableDeclaration ecdartext_etvariabledeclaration) {
        this.ecdartext_etvariabledeclaration = ecdartext_etvariabledeclaration;
    }

}