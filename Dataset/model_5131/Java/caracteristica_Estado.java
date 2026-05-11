





import java.util.List;
import java.util.ArrayList;

public class caracteristica_Estado  {

    private String nome;
    private boolean safe;





    private caracteristica_Simulacao caracteristica_simulacao;




    private caracteristica_CaracteristicaProduto caracteristica_caracteristicaproduto;




    private caracteristica_Transicao caracteristica_transicao;




    private caracteristica_Transicao caracteristica_transicao;


    public caracteristica_Estado(
        String nome,        boolean safe    ) {
        this.nome = nome;
        this.safe = safe;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public boolean getSafe() {
        return safe;
    }

    public void setSafe(boolean safe) {
        this.safe = safe;
    }

    public caracteristica_Simulacao getCaracteristica_simulacao() {
        return caracteristica_simulacao;
    }

    public void setCaracteristica_simulacao(caracteristica_Simulacao caracteristica_simulacao) {
        this.caracteristica_simulacao = caracteristica_simulacao;
    }
    public caracteristica_CaracteristicaProduto getCaracteristica_caracteristicaproduto() {
        return caracteristica_caracteristicaproduto;
    }

    public void setCaracteristica_caracteristicaproduto(caracteristica_CaracteristicaProduto caracteristica_caracteristicaproduto) {
        this.caracteristica_caracteristicaproduto = caracteristica_caracteristicaproduto;
    }
    public caracteristica_Transicao getCaracteristica_transicao() {
        return caracteristica_transicao;
    }

    public void setCaracteristica_transicao(caracteristica_Transicao caracteristica_transicao) {
        this.caracteristica_transicao = caracteristica_transicao;
    }
    public caracteristica_Transicao getCaracteristica_transicao() {
        return caracteristica_transicao;
    }

    public void setCaracteristica_transicao(caracteristica_Transicao caracteristica_transicao) {
        this.caracteristica_transicao = caracteristica_transicao;
    }

}