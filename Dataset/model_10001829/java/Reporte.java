





import java.util.List;
import java.util.ArrayList;

public class Reporte  {






    private List<Mascotas> mascotass;




    private List<Servicios> servicioss;


    public Reporte(
    ) {
        this.mascotass = new ArrayList<>();
        this.servicioss = new ArrayList<>();
    }

    public Reporte(
        ArrayList<Mascotas> mascotass,        ArrayList<Servicios> servicioss    ) {
        this.mascotass = mascotass;
        this.servicioss = servicioss;
    }


    public List<Mascotas> getMascotass() {
        return mascotass;
    }

    public void addMascotas(Mascotas mascotas) {
        this.mascotass.add(mascotas);
    }
    public List<Servicios> getServicioss() {
        return servicioss;
    }

    public void addServicios(Servicios servicios) {
        this.servicioss.add(servicios);
    }

}