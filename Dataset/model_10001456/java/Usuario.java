





import java.util.List;
import java.util.ArrayList;

public class Usuario  {

    private String passWord;
    private String userName;





    private List<Tarjeta> tarjetas;


    public Usuario(
        String passWord,        String userName    ) {
        this.passWord = passWord;
        this.userName = userName;
        this.tarjetas = new ArrayList<>();
    }

    public Usuario(
        String passWord,        String userName        ArrayList<Tarjeta> tarjetas    ) {
        this.passWord = passWord;
        this.userName = userName;
        this.tarjetas = tarjetas;
    }

    public String getPassword() {
        return passWord;
    }

    public void setPassword(String passWord) {
        this.passWord = passWord;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }

    public List<Tarjeta> getTarjetas() {
        return tarjetas;
    }

    public void addTarjeta(Tarjeta tarjeta) {
        this.tarjetas.add(tarjeta);
    }

}