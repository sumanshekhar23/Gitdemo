const { Pool } = require('pg');

async function run() {
  try {
    // Get inputs from the GitHub workflow
    const core = require('@actions/core');
    const dbHost = core.getInput('db_host');
    const dbUser = core.getInput('db_user');
    const dbPassword = core.getInput('db_password');
    const dbName = core.getInput('db_name');
    const dbPort = core.getInput('db_port');
    const tableName = core.getInput('table_name');
    const dataJson = core.getInput('data'); // Expected to be a JSON string

    const data = JSON.parse(dataJson);

    // Configure the PostgreSQL connection
    const pool = new Pool({
      host: dbHost,
      user: dbUser,
      password: dbPassword,
      database: dbName,
      port: dbPort,
    });

    // Build the SQL query
    const columns = Object.keys(data).join(', ');
    const values = Object.values(data);
    const placeholders = values.map((_, i) => `$${i + 1}`).join(', ');

    const query = `INSERT INTO ${tableName} (${columns}) VALUES (${placeholders}) RETURNING *`;

    // Execute the query
    const result = await pool.query(query, values);
    console.log('Inserted data:', result.rows[0]);

    // Close the pool
    await pool.end();

    // Set the output for the GitHub action
    core.setOutput('inserted_row', JSON.stringify(result.rows[0]));
  } catch (error) {
    console.error('Error:', error.message);
    const core = require('@actions/core');
    core.setFailed(error.message);
  }
}

run();
