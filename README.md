
<p align="center">
  <h3 align="center">Data Engineering Sensor Data</h3>

  <p align="center">
    A fully dockerized ELT pipeline project, using MYSQL, dbt, Apache Airflow, and Redash.
    <br />
    <a href="https://data-engineering-sensor-data.herokuapp.com/home.html"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/bereketkibru/Data_engineering_sensor_data">View Demo</a>
    ·
    <a href="https://github.com/bereketkibru/Data_engineering_sensor_data/issues">Report Bug</a>
    ·
    <a href="https://github.com/bereketkibru/Data_engineering_sensor_data/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Using a docker-compose file, developed a completely dockerized ELT pipeline with MySQL for data storage, Airflow for automation and orchestration, DBT for data transformation, and a Redash dashboard connected to the MySQL database.
### Built With

Tech Stack used in this project
* [MYSQL](https://dev.mysql.com/doc/)
* [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/)
* [dbt](https://docs.getdbt.com/)
* [Redash](https://redash.io/help/)


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bereketkibru/Data_engineering_sensor_data
   ```
2. Run
   ```sh
    docker-compose build
    docker-compose up
   ```
3. Open Airflow web browser
   ```JS
   Navigate to `http://localhost:8000/` on the browser
   activate and trigger dbt_load_dag
   activate and trigger dbt_dbt_dag
   ```
4. Access redash dashboard
   ```JS
   Navigate to `http://localhost:5000/` on the browser
   ```
5. Access your mysql database using adminar
   ```JS
   Navigate to `http://localhost:8080/` on the browser
   choose mysql databse
   use `root` for username
   use `pssd` for password
   ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Bereket Kibru - [@email](https://twitter.com/your_username) - bekakibru2@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [10 Academy](https://www.10academy.org/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/daniEL2371/sensor-data-ELT.svg?style=for-the-badge
[contributors-url]: https://github.com/bereketkibru/Data_engineering_sensor_data/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/daniEL2371/sensor-data-ELT.svg?style=for-the-badge
[forks-url]: https://github.com/bereketkibru/Data_engineering_sensor_data/network/members
[stars-shield]: https://img.shields.io/github/stars/daniEL2371/sensor-data-ELT.svg?style=for-the-badge
[stars-url]: https://github.com/bereketkibru/Data_engineering_sensor_data/stargazers
[issues-shield]: https://img.shields.io/github/issues/daniEL2371/sensor-data-ELT.svg?style=for-the-badge
[issues-url]: https://github.com/bereketkibru/Data_engineering_sensor_data/issues
[license-shield]: https://img.shields.io/github/license/daniEL2371/sensor-data-ELT.svg?style=for-the-badge
[license-url]: https://github.com/bereketkibru/Data_engineering_sensor_data/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: Capture.PNG
