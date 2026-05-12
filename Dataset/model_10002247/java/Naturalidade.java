





import java.util.List;
import java.util.ArrayList;

public class Naturalidade  {

    private String naturalidade;





    private List<Pessoa> pessoas;


    public Naturalidade(
        String naturalidade    ) {
        this.naturalidade = naturalidade;
        this.pessoas = new ArrayList<>();
    }

    public Naturalidade(
        String naturalidade        ArrayList<Pessoa> pessoas    ) {
        this.naturalidade = naturalidade;
        this.pessoas = pessoas;
    }

    public String getNaturalidade() {
        return naturalidade;
    }

    public void setNaturalidade(String naturalidade) {
        this.naturalidade = naturalidade;
    }

    public List<Pessoa> getPessoas() {
        return pessoas;
    }

    public void addPessoa(Pessoa pessoa) {
        this.pessoas.add(pessoa);
    }

}