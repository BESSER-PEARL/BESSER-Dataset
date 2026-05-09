





import java.util.List;
import java.util.ArrayList;

public class domain_TypePointer  {

    private String fakeTypeName;
    private String fakePackageName;



    public domain_TypePointer(
        String fakeTypeName,        String fakePackageName    ) {
        this.fakeTypeName = fakeTypeName;
        this.fakePackageName = fakePackageName;
    }


    public String getFaketypename() {
        return fakeTypeName;
    }

    public void setFaketypename(String fakeTypeName) {
        this.fakeTypeName = fakeTypeName;
    }
    public String getFakepackagename() {
        return fakePackageName;
    }

    public void setFakepackagename(String fakePackageName) {
        this.fakePackageName = fakePackageName;
    }


}