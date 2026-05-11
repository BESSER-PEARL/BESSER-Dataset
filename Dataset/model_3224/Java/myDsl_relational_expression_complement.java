





import java.util.List;
import java.util.ArrayList;

public class myDsl_relational_expression_complement  {

    private String menor_igual;
    private String maior_igual;
    private String maior;
    private String menor;



    public myDsl_relational_expression_complement(
        String menor_igual,        String maior_igual,        String maior,        String menor    ) {
        this.menor_igual = menor_igual;
        this.maior_igual = maior_igual;
        this.maior = maior;
        this.menor = menor;
    }


    public String getMenor_igual() {
        return menor_igual;
    }

    public void setMenor_igual(String menor_igual) {
        this.menor_igual = menor_igual;
    }
    public String getMaior_igual() {
        return maior_igual;
    }

    public void setMaior_igual(String maior_igual) {
        this.maior_igual = maior_igual;
    }
    public String getMaior() {
        return maior;
    }

    public void setMaior(String maior) {
        this.maior = maior;
    }
    public String getMenor() {
        return menor;
    }

    public void setMenor(String menor) {
        this.menor = menor;
    }


}