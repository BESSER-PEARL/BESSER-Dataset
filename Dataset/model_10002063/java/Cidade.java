





import java.util.List;
import java.util.ArrayList;

public class Cidade  {

    private String nome;
    private int ddd;
    private int codigo;





    private List<Paciente> pacientes;


    public Cidade(
        String nome,        int ddd,        int codigo    ) {
        this.nome = nome;
        this.ddd = ddd;
        this.codigo = codigo;
        this.pacientes = new ArrayList<>();
    }

    public Cidade(
        String nome,        int ddd,        int codigo        ArrayList<Paciente> pacientes    ) {
        this.nome = nome;
        this.ddd = ddd;
        this.codigo = codigo;
        this.pacientes = pacientes;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getDdd() {
        return ddd;
    }

    public void setDdd(int ddd) {
        this.ddd = ddd;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public List<Paciente> getPacientes() {
        return pacientes;
    }

    public void addPaciente(Paciente paciente) {
        this.pacientes.add(paciente);
    }

}