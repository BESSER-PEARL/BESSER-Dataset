





import java.util.List;
import java.util.ArrayList;

public class IAutenticavel  {

    private String Autenticar;





    private IAutenticavel iautenticavel;


    public IAutenticavel(
        String Autenticar    ) {
        this.Autenticar = Autenticar;
    }


    public String getAutenticar() {
        return Autenticar;
    }

    public void setAutenticar(String Autenticar) {
        this.Autenticar = Autenticar;
    }

    public IAutenticavel getIautenticavel() {
        return iautenticavel;
    }

    public void setIautenticavel(IAutenticavel iautenticavel) {
        this.iautenticavel = iautenticavel;
    }

}