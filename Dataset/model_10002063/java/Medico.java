





import java.util.List;
import java.util.ArrayList;

public class Medico  {

    private String nome;
    private int crm;





    private List<Pedido_Exame> pedido_exames;


    public Medico(
        String nome,        int crm    ) {
        this.nome = nome;
        this.crm = crm;
        this.pedido_exames = new ArrayList<>();
    }

    public Medico(
        String nome,        int crm        ArrayList<Pedido_Exame> pedido_exames    ) {
        this.nome = nome;
        this.crm = crm;
        this.pedido_exames = pedido_exames;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getCrm() {
        return crm;
    }

    public void setCrm(int crm) {
        this.crm = crm;
    }

    public List<Pedido_Exame> getPedido_exames() {
        return pedido_exames;
    }

    public void addPedido_exame(Pedido_exame pedido_exame) {
        this.pedido_exames.add(pedido_exame);
    }

}