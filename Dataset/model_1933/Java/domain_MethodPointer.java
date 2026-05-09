





import java.util.List;
import java.util.ArrayList;

public class domain_MethodPointer extends TypePointer {

    private String fakeMethod;



    public domain_MethodPointer(
        String fakeMethod    ) {
        super(
        );
        this.fakeMethod = fakeMethod;
    }


    public String getFakemethod() {
        return fakeMethod;
    }

    public void setFakemethod(String fakeMethod) {
        this.fakeMethod = fakeMethod;
    }


}