





import java.util.List;
import java.util.ArrayList;

public class DispositivoBluetooth  {

    private String macAddress;
    private String nome;



    public DispositivoBluetooth(
        String macAddress,        String nome    ) {
        this.macAddress = macAddress;
        this.nome = nome;
    }


    public String getMacaddress() {
        return macAddress;
    }

    public void setMacaddress(String macAddress) {
        this.macAddress = macAddress;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }


}