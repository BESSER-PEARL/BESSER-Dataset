





import java.util.List;
import java.util.ArrayList;

public class SistemaApuesta  {






    private List<Apuesta> apuestas;




    private List<Usuario> usuarios;




    private List<Partido> partidos;


    public SistemaApuesta(
    ) {
        this.apuestas = new ArrayList<>();
        this.usuarios = new ArrayList<>();
        this.partidos = new ArrayList<>();
    }

    public SistemaApuesta(
        ArrayList<Apuesta> apuestas,        ArrayList<Usuario> usuarios,        ArrayList<Partido> partidos    ) {
        this.apuestas = apuestas;
        this.usuarios = usuarios;
        this.partidos = partidos;
    }


    public List<Apuesta> getApuestas() {
        return apuestas;
    }

    public void addApuesta(Apuesta apuesta) {
        this.apuestas.add(apuesta);
    }
    public List<Usuario> getUsuarios() {
        return usuarios;
    }

    public void addUsuario(Usuario usuario) {
        this.usuarios.add(usuario);
    }
    public List<Partido> getPartidos() {
        return partidos;
    }

    public void addPartido(Partido partido) {
        this.partidos.add(partido);
    }

}