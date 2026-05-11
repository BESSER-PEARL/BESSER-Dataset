





import java.util.List;
import java.util.ArrayList;

public class cm_repository_Interface extends Entity {






    private Repository repository;




    private List<Signature> signatures;




    private List<Interface> interfaces;


    public cm_repository_Interface(
    ) {
        super(
        );
        this.signatures = new ArrayList<>();
        this.interfaces = new ArrayList<>();
    }

    public cm_repository_Interface(
        ArrayList<Signature> signatures,        ArrayList<Interface> interfaces    ) {
        this.signatures = signatures;
        this.interfaces = interfaces;
    }


    public Repository getRepository() {
        return repository;
    }

    public void setRepository(Repository repository) {
        this.repository = repository;
    }
    public List<Signature> getSignatures() {
        return signatures;
    }

    public void addSignature(Signature signature) {
        this.signatures.add(signature);
    }
    public List<Interface> getInterfaces() {
        return interfaces;
    }

    public void addInterface(Interface interface) {
        this.interfaces.add(interface);
    }

}