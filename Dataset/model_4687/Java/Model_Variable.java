





import java.util.List;
import java.util.ArrayList;

public class Model_Variable  {

    private String domain;
    private String name;





    private Model_AtomicDEVS model_atomicdevs;


    public Model_Variable(
        String domain,        String name    ) {
        this.domain = domain;
        this.name = name;
    }


    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Model_AtomicDEVS getModel_atomicdevs() {
        return model_atomicdevs;
    }

    public void setModel_atomicdevs(Model_AtomicDEVS model_atomicdevs) {
        this.model_atomicdevs = model_atomicdevs;
    }

}