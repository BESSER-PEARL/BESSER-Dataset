





import java.util.List;
import java.util.ArrayList;

public class kmLogo_JavaProgram  {

    private String name;





    private List<kmLogo_MethodeDeclaration> kmlogo_methodedeclarations;


    public kmLogo_JavaProgram(
        String name    ) {
        this.name = name;
        this.kmlogo_methodedeclarations = new ArrayList<>();
    }

    public kmLogo_JavaProgram(
        String name        ArrayList<kmLogo_MethodeDeclaration> kmlogo_methodedeclarations    ) {
        this.name = name;
        this.kmlogo_methodedeclarations = kmlogo_methodedeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<kmLogo_MethodeDeclaration> getKmlogo_methodedeclarations() {
        return kmlogo_methodedeclarations;
    }

    public void addKmlogo_methodedeclaration(Kmlogo_methodedeclaration kmlogo_methodedeclaration) {
        this.kmlogo_methodedeclarations.add(kmlogo_methodedeclaration);
    }

}