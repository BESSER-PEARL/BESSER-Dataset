





import java.util.List;
import java.util.ArrayList;

public class ContaBancaria  {

    private int NumeroConta;
    private String NomeConta;
    private float Saldo;





    private Banco banco;


    public ContaBancaria(
        int NumeroConta,        String NomeConta,        float Saldo    ) {
        this.NumeroConta = NumeroConta;
        this.NomeConta = NomeConta;
        this.Saldo = Saldo;
    }


    public int getNumeroconta() {
        return NumeroConta;
    }

    public void setNumeroconta(int NumeroConta) {
        this.NumeroConta = NumeroConta;
    }
    public String getNomeconta() {
        return NomeConta;
    }

    public void setNomeconta(String NomeConta) {
        this.NomeConta = NomeConta;
    }
    public float getSaldo() {
        return Saldo;
    }

    public void setSaldo(float Saldo) {
        this.Saldo = Saldo;
    }

    public Banco getBanco() {
        return banco;
    }

    public void setBanco(Banco banco) {
        this.banco = banco;
    }

}