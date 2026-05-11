





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETTypeID  {

    private String name;





    private ecdarText_ETTypeDeclaration ecdartext_ettypedeclaration;


    public ecdarText_ETTypeID(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecdarText_ETTypeDeclaration getEcdartext_ettypedeclaration() {
        return ecdartext_ettypedeclaration;
    }

    public void setEcdartext_ettypedeclaration(ecdarText_ETTypeDeclaration ecdartext_ettypedeclaration) {
        this.ecdartext_ettypedeclaration = ecdartext_ettypedeclaration;
    }

}