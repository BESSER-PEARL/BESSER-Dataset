





import java.util.List;
import java.util.ArrayList;

public class java__NamedElement extends ASTNode {

    private boolean proxy;
    private String name;



    public java__NamedElement(
        boolean proxy,        String name    ) {
        super(
        );
        this.proxy = proxy;
        this.name = name;
    }


    public boolean getProxy() {
        return proxy;
    }

    public void setProxy(boolean proxy) {
        this.proxy = proxy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}