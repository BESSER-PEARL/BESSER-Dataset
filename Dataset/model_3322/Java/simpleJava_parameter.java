





import java.util.List;
import java.util.ArrayList;

public class simpleJava_parameter  {

    private String nomeParametro;





    private simpleJava_parameter_list simplejava_parameter_list;




    private simpleJava_type simplejava_type;


    public simpleJava_parameter(
        String nomeParametro    ) {
        this.nomeParametro = nomeParametro;
    }


    public String getNomeparametro() {
        return nomeParametro;
    }

    public void setNomeparametro(String nomeParametro) {
        this.nomeParametro = nomeParametro;
    }

    public simpleJava_parameter_list getSimplejava_parameter_list() {
        return simplejava_parameter_list;
    }

    public void setSimplejava_parameter_list(simpleJava_parameter_list simplejava_parameter_list) {
        this.simplejava_parameter_list = simplejava_parameter_list;
    }
    public simpleJava_type getSimplejava_type() {
        return simplejava_type;
    }

    public void setSimplejava_type(simpleJava_type simplejava_type) {
        this.simplejava_type = simplejava_type;
    }

}