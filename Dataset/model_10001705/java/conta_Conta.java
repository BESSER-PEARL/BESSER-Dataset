





import java.util.List;
import java.util.ArrayList;

public class conta_Conta  {

    private None tipo;
    private float saldo;





    private cliente_Customer cliente_customer;




    private List<transacao_transacao> transacao_transacaos;


    public conta_Conta(
        None tipo,        float saldo    ) {
        this.tipo = tipo;
        this.saldo = saldo;
        this.transacao_transacaos = new ArrayList<>();
    }

    public conta_Conta(
        None tipo,        float saldo        ArrayList<transacao_transacao> transacao_transacaos    ) {
        this.tipo = tipo;
        this.saldo = saldo;
        this.transacao_transacaos = transacao_transacaos;
    }

    public None getTipo() {
        return tipo;
    }

    public void setTipo(None tipo) {
        this.tipo = tipo;
    }
    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public cliente_Customer getCliente_customer() {
        return cliente_customer;
    }

    public void setCliente_customer(cliente_Customer cliente_customer) {
        this.cliente_customer = cliente_customer;
    }
    public List<transacao_transacao> getTransacao_transacaos() {
        return transacao_transacaos;
    }

    public void addTransacao_transacao(Transacao_transacao transacao_transacao) {
        this.transacao_transacaos.add(transacao_transacao);
    }

}