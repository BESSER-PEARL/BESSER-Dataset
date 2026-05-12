





import java.util.List;
import java.util.ArrayList;

public class MedicaoBatimento  {

    private None usuario;
    private None treino;
    private int valor;
    private String instante;
    private boolean enviado;



    public MedicaoBatimento(
        None usuario,        None treino,        int valor,        String instante,        boolean enviado    ) {
        this.usuario = usuario;
        this.treino = treino;
        this.valor = valor;
        this.instante = instante;
        this.enviado = enviado;
    }


    public None getUsuario() {
        return usuario;
    }

    public void setUsuario(None usuario) {
        this.usuario = usuario;
    }
    public None getTreino() {
        return treino;
    }

    public void setTreino(None treino) {
        this.treino = treino;
    }
    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }
    public String getInstante() {
        return instante;
    }

    public void setInstante(String instante) {
        this.instante = instante;
    }
    public boolean getEnviado() {
        return enviado;
    }

    public void setEnviado(boolean enviado) {
        this.enviado = enviado;
    }


}