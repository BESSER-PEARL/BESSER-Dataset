





import java.util.List;
import java.util.ArrayList;

public class UML2_PrimitiveFunction extends PackageableElement {

    private String language;
    private String body;



    public UML2_PrimitiveFunction(
        String language,        String body    ) {
        super(
        );
        this.language = language;
        this.body = body;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }


}