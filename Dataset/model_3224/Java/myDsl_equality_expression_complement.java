





import java.util.List;
import java.util.ArrayList;

public class myDsl_equality_expression_complement  {

    private String menor_igual;
    private String maior;
    private String maior_igual;
    private String igual;
    private String menor;
    private String n_igual;





    private myDsl_equality_expression_linha mydsl_equality_expression_linha;




    private myDsl_relational_expression mydsl_relational_expression;


    public myDsl_equality_expression_complement(
        String menor_igual,        String maior,        String maior_igual,        String igual,        String menor,        String n_igual    ) {
        this.menor_igual = menor_igual;
        this.maior = maior;
        this.maior_igual = maior_igual;
        this.igual = igual;
        this.menor = menor;
        this.n_igual = n_igual;
    }


    public String getMenor_igual() {
        return menor_igual;
    }

    public void setMenor_igual(String menor_igual) {
        this.menor_igual = menor_igual;
    }
    public String getMaior() {
        return maior;
    }

    public void setMaior(String maior) {
        this.maior = maior;
    }
    public String getMaior_igual() {
        return maior_igual;
    }

    public void setMaior_igual(String maior_igual) {
        this.maior_igual = maior_igual;
    }
    public String getIgual() {
        return igual;
    }

    public void setIgual(String igual) {
        this.igual = igual;
    }
    public String getMenor() {
        return menor;
    }

    public void setMenor(String menor) {
        this.menor = menor;
    }
    public String getN_igual() {
        return n_igual;
    }

    public void setN_igual(String n_igual) {
        this.n_igual = n_igual;
    }

    public myDsl_equality_expression_linha getMydsl_equality_expression_linha() {
        return mydsl_equality_expression_linha;
    }

    public void setMydsl_equality_expression_linha(myDsl_equality_expression_linha mydsl_equality_expression_linha) {
        this.mydsl_equality_expression_linha = mydsl_equality_expression_linha;
    }
    public myDsl_relational_expression getMydsl_relational_expression() {
        return mydsl_relational_expression;
    }

    public void setMydsl_relational_expression(myDsl_relational_expression mydsl_relational_expression) {
        this.mydsl_relational_expression = mydsl_relational_expression;
    }

}