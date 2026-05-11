





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETFile  {






    private List<ecdarText_ETSpecification> ecdartext_etspecifications;




    private ecdarText_ETDeclarations ecdartext_etdeclarations;


    public ecdarText_ETFile(
    ) {
        this.ecdartext_etspecifications = new ArrayList<>();
    }

    public ecdarText_ETFile(
        ArrayList<ecdarText_ETSpecification> ecdartext_etspecifications    ) {
        this.ecdartext_etspecifications = ecdartext_etspecifications;
    }


    public List<ecdarText_ETSpecification> getEcdartext_etspecifications() {
        return ecdartext_etspecifications;
    }

    public void addEcdartext_etspecification(Ecdartext_etspecification ecdartext_etspecification) {
        this.ecdartext_etspecifications.add(ecdartext_etspecification);
    }
    public ecdarText_ETDeclarations getEcdartext_etdeclarations() {
        return ecdartext_etdeclarations;
    }

    public void setEcdartext_etdeclarations(ecdarText_ETDeclarations ecdartext_etdeclarations) {
        this.ecdartext_etdeclarations = ecdartext_etdeclarations;
    }

}