





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETTypeID  {

    private String name;





    private List<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations;




    private ecdarText_ETTypeDeclaration ecdartext_ettypedeclaration;


    public ecdarText_ETTypeID(
        String name    ) {
        this.name = name;
        this.ecdartext_etarraydeclarations = new ArrayList<>();
    }

    public ecdarText_ETTypeID(
        String name        ArrayList<ecdarText_ETArrayDeclaration> ecdartext_etarraydeclarations    ) {
        this.name = name;
        this.ecdartext_etarraydeclarations = ecdartext_etarraydeclarations;
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
    public ecdarText_ETTypeDeclaration getEcdartext_ettypedeclaration() {
        return ecdartext_ettypedeclaration;
    }

    public void setEcdartext_ettypedeclaration(ecdarText_ETTypeDeclaration ecdartext_ettypedeclaration) {
        this.ecdartext_ettypedeclaration = ecdartext_ettypedeclaration;
    }

}