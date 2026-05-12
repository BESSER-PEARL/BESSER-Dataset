





import java.util.List;
import java.util.ArrayList;

public class Exame  {

    private float valor;
    private String descricao;
    private String procedimentos;
    private int codigo;



    public Exame(
        float valor,        String descricao,        String procedimentos,        int codigo    ) {
        this.valor = valor;
        this.descricao = descricao;
        this.procedimentos = procedimentos;
        this.codigo = codigo;
    }


    public float getValor() {
        return valor;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }
    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public String getProcedimentos() {
        return procedimentos;
    }

    public void setProcedimentos(String procedimentos) {
        this.procedimentos = procedimentos;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }


}