





import java.util.List;
import java.util.ArrayList;

public class Entrega_producto  {

    private String Email_confirmaci_n;
    private String Agradecimiento;





    private List<Lineamiento> lineamientos;


    public Entrega_producto(
        String Email_confirmaci_n,        String Agradecimiento    ) {
        this.Email_confirmaci_n = Email_confirmaci_n;
        this.Agradecimiento = Agradecimiento;
        this.lineamientos = new ArrayList<>();
    }

    public Entrega_producto(
        String Email_confirmaci_n,        String Agradecimiento        ArrayList<Lineamiento> lineamientos    ) {
        this.Email_confirmaci_n = Email_confirmaci_n;
        this.Agradecimiento = Agradecimiento;
        this.lineamientos = lineamientos;
    }

    public String getEmail_confirmaci_n() {
        return Email_confirmaci_n;
    }

    public void setEmail_confirmaci_n(String Email_confirmaci_n) {
        this.Email_confirmaci_n = Email_confirmaci_n;
    }
    public String getAgradecimiento() {
        return Agradecimiento;
    }

    public void setAgradecimiento(String Agradecimiento) {
        this.Agradecimiento = Agradecimiento;
    }

    public List<Lineamiento> getLineamientos() {
        return lineamientos;
    }

    public void addLineamiento(Lineamiento lineamiento) {
        this.lineamientos.add(lineamiento);
    }

}