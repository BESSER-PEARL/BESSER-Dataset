





import java.util.List;
import java.util.ArrayList;

public class Java5_NamedElement extends ASTNode {

    private String name;
    private boolean proxy;



    public Java5_NamedElement(
        String name,        boolean proxy    ) {
        super(
        );
        this.name = name;
        this.proxy = proxy;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }


}